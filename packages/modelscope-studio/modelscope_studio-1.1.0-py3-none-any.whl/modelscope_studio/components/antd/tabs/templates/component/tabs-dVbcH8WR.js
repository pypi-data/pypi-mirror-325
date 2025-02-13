import { i as de, a as A, r as fe, g as me, w as O, b as pe } from "./Index-CpV3-R4f.js";
const y = window.ms_globals.React, le = window.ms_globals.React.forwardRef, ae = window.ms_globals.React.useRef, ce = window.ms_globals.React.useState, ue = window.ms_globals.React.useEffect, $ = window.ms_globals.React.useMemo, W = window.ms_globals.ReactDOM.createPortal, _e = window.ms_globals.internalContext.useContextPropsContext, k = window.ms_globals.internalContext.ContextPropsProvider, he = window.ms_globals.antd.Tabs, ge = window.ms_globals.createItemsContext.createItemsContext;
var be = /\s/;
function xe(e) {
  for (var t = e.length; t-- && be.test(e.charAt(t)); )
    ;
  return t;
}
var Ce = /^\s+/;
function Ee(e) {
  return e && e.slice(0, xe(e) + 1).replace(Ce, "");
}
var U = NaN, we = /^[-+]0x[0-9a-f]+$/i, ve = /^0b[01]+$/i, ye = /^0o[0-7]+$/i, Ie = parseInt;
function H(e) {
  if (typeof e == "number")
    return e;
  if (de(e))
    return U;
  if (A(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = A(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = Ee(e);
  var s = ve.test(e);
  return s || ye.test(e) ? Ie(e.slice(2), s ? 2 : 8) : we.test(e) ? U : +e;
}
var L = function() {
  return fe.Date.now();
}, Se = "Expected a function", Te = Math.max, Re = Math.min;
function Oe(e, t, s) {
  var i, n, r, o, l, c, h = 0, g = !1, a = !1, m = !0;
  if (typeof e != "function")
    throw new TypeError(Se);
  t = H(t) || 0, A(s) && (g = !!s.leading, a = "maxWait" in s, r = a ? Te(H(s.maxWait) || 0, t) : r, m = "trailing" in s ? !!s.trailing : m);
  function u(_) {
    var v = i, R = n;
    return i = n = void 0, h = _, o = e.apply(R, v), o;
  }
  function C(_) {
    return h = _, l = setTimeout(b, t), g ? u(_) : o;
  }
  function f(_) {
    var v = _ - c, R = _ - h, D = t - v;
    return a ? Re(D, r - R) : D;
  }
  function p(_) {
    var v = _ - c, R = _ - h;
    return c === void 0 || v >= t || v < 0 || a && R >= r;
  }
  function b() {
    var _ = L();
    if (p(_))
      return w(_);
    l = setTimeout(b, f(_));
  }
  function w(_) {
    return l = void 0, m && i ? u(_) : (i = n = void 0, o);
  }
  function I() {
    l !== void 0 && clearTimeout(l), h = 0, i = c = n = l = void 0;
  }
  function d() {
    return l === void 0 ? o : w(L());
  }
  function S() {
    var _ = L(), v = p(_);
    if (i = arguments, n = this, c = _, v) {
      if (l === void 0)
        return C(c);
      if (a)
        return clearTimeout(l), l = setTimeout(b, t), u(c);
    }
    return l === void 0 && (l = setTimeout(b, t)), o;
  }
  return S.cancel = I, S.flush = d, S;
}
var ee = {
  exports: {}
}, B = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var Pe = y, je = Symbol.for("react.element"), ke = Symbol.for("react.fragment"), Be = Object.prototype.hasOwnProperty, Le = Pe.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, Fe = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function te(e, t, s) {
  var i, n = {}, r = null, o = null;
  s !== void 0 && (r = "" + s), t.key !== void 0 && (r = "" + t.key), t.ref !== void 0 && (o = t.ref);
  for (i in t) Be.call(t, i) && !Fe.hasOwnProperty(i) && (n[i] = t[i]);
  if (e && e.defaultProps) for (i in t = e.defaultProps, t) n[i] === void 0 && (n[i] = t[i]);
  return {
    $$typeof: je,
    type: e,
    key: r,
    ref: o,
    props: n,
    _owner: Le.current
  };
}
B.Fragment = ke;
B.jsx = te;
B.jsxs = te;
ee.exports = B;
var x = ee.exports;
const {
  SvelteComponent: Ne,
  assign: G,
  binding_callbacks: q,
  check_outros: We,
  children: ne,
  claim_element: re,
  claim_space: Ae,
  component_subscribe: V,
  compute_slots: Me,
  create_slot: ze,
  detach: T,
  element: oe,
  empty: J,
  exclude_internal_props: X,
  get_all_dirty_from_scope: De,
  get_slot_changes: Ue,
  group_outros: He,
  init: Ge,
  insert_hydration: P,
  safe_not_equal: qe,
  set_custom_element_data: se,
  space: Ve,
  transition_in: j,
  transition_out: M,
  update_slot_base: Je
} = window.__gradio__svelte__internal, {
  beforeUpdate: Xe,
  getContext: Ye,
  onDestroy: Ke,
  setContext: Qe
} = window.__gradio__svelte__internal;
function Y(e) {
  let t, s;
  const i = (
    /*#slots*/
    e[7].default
  ), n = ze(
    i,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = oe("svelte-slot"), n && n.c(), this.h();
    },
    l(r) {
      t = re(r, "SVELTE-SLOT", {
        class: !0
      });
      var o = ne(t);
      n && n.l(o), o.forEach(T), this.h();
    },
    h() {
      se(t, "class", "svelte-1rt0kpf");
    },
    m(r, o) {
      P(r, t, o), n && n.m(t, null), e[9](t), s = !0;
    },
    p(r, o) {
      n && n.p && (!s || o & /*$$scope*/
      64) && Je(
        n,
        i,
        r,
        /*$$scope*/
        r[6],
        s ? Ue(
          i,
          /*$$scope*/
          r[6],
          o,
          null
        ) : De(
          /*$$scope*/
          r[6]
        ),
        null
      );
    },
    i(r) {
      s || (j(n, r), s = !0);
    },
    o(r) {
      M(n, r), s = !1;
    },
    d(r) {
      r && T(t), n && n.d(r), e[9](null);
    }
  };
}
function Ze(e) {
  let t, s, i, n, r = (
    /*$$slots*/
    e[4].default && Y(e)
  );
  return {
    c() {
      t = oe("react-portal-target"), s = Ve(), r && r.c(), i = J(), this.h();
    },
    l(o) {
      t = re(o, "REACT-PORTAL-TARGET", {
        class: !0
      }), ne(t).forEach(T), s = Ae(o), r && r.l(o), i = J(), this.h();
    },
    h() {
      se(t, "class", "svelte-1rt0kpf");
    },
    m(o, l) {
      P(o, t, l), e[8](t), P(o, s, l), r && r.m(o, l), P(o, i, l), n = !0;
    },
    p(o, [l]) {
      /*$$slots*/
      o[4].default ? r ? (r.p(o, l), l & /*$$slots*/
      16 && j(r, 1)) : (r = Y(o), r.c(), j(r, 1), r.m(i.parentNode, i)) : r && (He(), M(r, 1, 1, () => {
        r = null;
      }), We());
    },
    i(o) {
      n || (j(r), n = !0);
    },
    o(o) {
      M(r), n = !1;
    },
    d(o) {
      o && (T(t), T(s), T(i)), e[8](null), r && r.d(o);
    }
  };
}
function K(e) {
  const {
    svelteInit: t,
    ...s
  } = e;
  return s;
}
function $e(e, t, s) {
  let i, n, {
    $$slots: r = {},
    $$scope: o
  } = t;
  const l = Me(r);
  let {
    svelteInit: c
  } = t;
  const h = O(K(t)), g = O();
  V(e, g, (d) => s(0, i = d));
  const a = O();
  V(e, a, (d) => s(1, n = d));
  const m = [], u = Ye("$$ms-gr-react-wrapper"), {
    slotKey: C,
    slotIndex: f,
    subSlotIndex: p
  } = me() || {}, b = c({
    parent: u,
    props: h,
    target: g,
    slot: a,
    slotKey: C,
    slotIndex: f,
    subSlotIndex: p,
    onDestroy(d) {
      m.push(d);
    }
  });
  Qe("$$ms-gr-react-wrapper", b), Xe(() => {
    h.set(K(t));
  }), Ke(() => {
    m.forEach((d) => d());
  });
  function w(d) {
    q[d ? "unshift" : "push"](() => {
      i = d, g.set(i);
    });
  }
  function I(d) {
    q[d ? "unshift" : "push"](() => {
      n = d, a.set(n);
    });
  }
  return e.$$set = (d) => {
    s(17, t = G(G({}, t), X(d))), "svelteInit" in d && s(5, c = d.svelteInit), "$$scope" in d && s(6, o = d.$$scope);
  }, t = X(t), [i, n, g, a, l, c, o, r, w, I];
}
class et extends Ne {
  constructor(t) {
    super(), Ge(this, t, $e, Ze, qe, {
      svelteInit: 5
    });
  }
}
const Q = window.ms_globals.rerender, F = window.ms_globals.tree;
function tt(e, t = {}) {
  function s(i) {
    const n = O(), r = new et({
      ...i,
      props: {
        svelteInit(o) {
          window.ms_globals.autokey += 1;
          const l = {
            key: window.ms_globals.autokey,
            svelteInstance: n,
            reactComponent: e,
            props: o.props,
            slot: o.slot,
            target: o.target,
            slotIndex: o.slotIndex,
            subSlotIndex: o.subSlotIndex,
            ignore: t.ignore,
            slotKey: o.slotKey,
            nodes: []
          }, c = o.parent ?? F;
          return c.nodes = [...c.nodes, l], Q({
            createPortal: W,
            node: F
          }), o.onDestroy(() => {
            c.nodes = c.nodes.filter((h) => h.svelteInstance !== n), Q({
              createPortal: W,
              node: F
            });
          }), l;
        },
        ...i.props
      }
    });
    return n.set(r), r;
  }
  return new Promise((i) => {
    window.ms_globals.initializePromise.then(() => {
      i(s);
    });
  });
}
const nt = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function rt(e) {
  return e ? Object.keys(e).reduce((t, s) => {
    const i = e[s];
    return t[s] = ot(s, i), t;
  }, {}) : {};
}
function ot(e, t) {
  return typeof t == "number" && !nt.includes(e) ? t + "px" : t;
}
function z(e) {
  const t = [], s = e.cloneNode(!1);
  if (e._reactElement) {
    const n = y.Children.toArray(e._reactElement.props.children).map((r) => {
      if (y.isValidElement(r) && r.props.__slot__) {
        const {
          portals: o,
          clonedElement: l
        } = z(r.props.el);
        return y.cloneElement(r, {
          ...r.props,
          el: l,
          children: [...y.Children.toArray(r.props.children), ...o]
        });
      }
      return null;
    });
    return n.originalChildren = e._reactElement.props.children, t.push(W(y.cloneElement(e._reactElement, {
      ...e._reactElement.props,
      children: n
    }), s)), {
      clonedElement: s,
      portals: t
    };
  }
  Object.keys(e.getEventListeners()).forEach((n) => {
    e.getEventListeners(n).forEach(({
      listener: o,
      type: l,
      useCapture: c
    }) => {
      s.addEventListener(l, o, c);
    });
  });
  const i = Array.from(e.childNodes);
  for (let n = 0; n < i.length; n++) {
    const r = i[n];
    if (r.nodeType === 1) {
      const {
        clonedElement: o,
        portals: l
      } = z(r);
      t.push(...l), s.appendChild(o);
    } else r.nodeType === 3 && s.appendChild(r.cloneNode());
  }
  return {
    clonedElement: s,
    portals: t
  };
}
function st(e, t) {
  e && (typeof e == "function" ? e(t) : e.current = t);
}
const E = le(({
  slot: e,
  clone: t,
  className: s,
  style: i,
  observeAttributes: n
}, r) => {
  const o = ae(), [l, c] = ce([]), {
    forceClone: h
  } = _e(), g = h ? !0 : t;
  return ue(() => {
    var C;
    if (!o.current || !e)
      return;
    let a = e;
    function m() {
      let f = a;
      if (a.tagName.toLowerCase() === "svelte-slot" && a.children.length === 1 && a.children[0] && (f = a.children[0], f.tagName.toLowerCase() === "react-portal-target" && f.children[0] && (f = f.children[0])), st(r, f), s && f.classList.add(...s.split(" ")), i) {
        const p = rt(i);
        Object.keys(p).forEach((b) => {
          f.style[b] = p[b];
        });
      }
    }
    let u = null;
    if (g && window.MutationObserver) {
      let f = function() {
        var I, d, S;
        (I = o.current) != null && I.contains(a) && ((d = o.current) == null || d.removeChild(a));
        const {
          portals: b,
          clonedElement: w
        } = z(e);
        a = w, c(b), a.style.display = "contents", m(), (S = o.current) == null || S.appendChild(a);
      };
      f();
      const p = Oe(() => {
        f(), u == null || u.disconnect(), u == null || u.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: n
        });
      }, 50);
      u = new window.MutationObserver(p), u.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      a.style.display = "contents", m(), (C = o.current) == null || C.appendChild(a);
    return () => {
      var f, p;
      a.style.display = "", (f = o.current) != null && f.contains(a) && ((p = o.current) == null || p.removeChild(a)), u == null || u.disconnect();
    };
  }, [e, g, s, i, r, n]), y.createElement("react-child", {
    ref: o,
    style: {
      display: "contents"
    }
  }, ...l);
});
function it(e) {
  return /^(?:async\s+)?(?:function\s*(?:\w*\s*)?\(|\([\w\s,=]*\)\s*=>|\(\{[\w\s,=]*\}\)\s*=>|function\s*\*\s*\w*\s*\()/i.test(e.trim());
}
function lt(e, t = !1) {
  try {
    if (pe(e))
      return e;
    if (t && !it(e))
      return;
    if (typeof e == "string") {
      let s = e.trim();
      return s.startsWith(";") && (s = s.slice(1)), s.endsWith(";") && (s = s.slice(0, -1)), new Function(`return (...args) => (${s})(...args)`)();
    }
    return;
  } catch {
    return;
  }
}
function N(e, t) {
  return $(() => lt(e, t), [e, t]);
}
function at(e) {
  return Object.keys(e).reduce((t, s) => (e[s] !== void 0 && (t[s] = e[s]), t), {});
}
function ie(e, t, s) {
  const i = e.filter(Boolean);
  if (i.length !== 0)
    return i.map((n, r) => {
      var h;
      if (typeof n != "object")
        return n;
      const o = {
        ...n.props,
        key: ((h = n.props) == null ? void 0 : h.key) ?? (s ? `${s}-${r}` : `${r}`)
      };
      let l = o;
      Object.keys(n.slots).forEach((g) => {
        if (!n.slots[g] || !(n.slots[g] instanceof Element) && !n.slots[g].el)
          return;
        const a = g.split(".");
        a.forEach((b, w) => {
          l[b] || (l[b] = {}), w !== a.length - 1 && (l = o[b]);
        });
        const m = n.slots[g];
        let u, C, f = !1, p = t == null ? void 0 : t.forceClone;
        m instanceof Element ? u = m : (u = m.el, C = m.callback, f = m.clone ?? f, p = m.forceClone ?? p), p = p ?? !!C, l[a[a.length - 1]] = u ? C ? (...b) => (C(a[a.length - 1], b), /* @__PURE__ */ x.jsx(k, {
          params: b,
          forceClone: p,
          children: /* @__PURE__ */ x.jsx(E, {
            slot: u,
            clone: f
          })
        })) : /* @__PURE__ */ x.jsx(k, {
          forceClone: p,
          children: /* @__PURE__ */ x.jsx(E, {
            slot: u,
            clone: f
          })
        }) : l[a[a.length - 1]], l = o;
      });
      const c = "children";
      return n[c] && (o[c] = ie(n[c], t, `${r}`)), o;
    });
}
function Z(e, t) {
  return e ? /* @__PURE__ */ x.jsx(E, {
    slot: e,
    clone: t == null ? void 0 : t.clone
  }) : null;
}
function ct({
  key: e,
  slots: t,
  targets: s
}, i) {
  return t[e] ? (...n) => s ? s.map((r, o) => /* @__PURE__ */ x.jsx(k, {
    params: n,
    forceClone: !0,
    children: Z(r, {
      clone: !0,
      ...i
    })
  }, o)) : /* @__PURE__ */ x.jsx(k, {
    params: n,
    forceClone: !0,
    children: Z(t[e], {
      clone: !0,
      ...i
    })
  }) : void 0;
}
const {
  withItemsContextProvider: ut,
  useItems: dt,
  ItemHandler: mt
} = ge("antd-tabs-items"), pt = tt(ut(["items", "default"], ({
  slots: e,
  indicator: t,
  items: s,
  onChange: i,
  more: n,
  children: r,
  renderTabBar: o,
  setSlotParams: l,
  ...c
}) => {
  const h = N(t == null ? void 0 : t.size), g = N(n == null ? void 0 : n.getPopupContainer), a = N(o), {
    items: m
  } = dt(), u = m.items.length > 0 ? m.items : m.default;
  return /* @__PURE__ */ x.jsxs(x.Fragment, {
    children: [/* @__PURE__ */ x.jsx("div", {
      style: {
        display: "none"
      },
      children: r
    }), /* @__PURE__ */ x.jsx(he, {
      ...c,
      indicator: h ? {
        ...t,
        size: h
      } : t,
      renderTabBar: e.renderTabBar ? ct({
        slots: e,
        setSlotParams: l,
        key: "renderTabBar"
      }) : a,
      items: $(() => s || ie(u), [s, u]),
      more: at({
        ...n || {},
        getPopupContainer: g || (n == null ? void 0 : n.getPopupContainer),
        icon: e["more.icon"] ? /* @__PURE__ */ x.jsx(E, {
          slot: e["more.icon"]
        }) : n == null ? void 0 : n.icon
      }),
      tabBarExtraContent: e.tabBarExtraContent ? /* @__PURE__ */ x.jsx(E, {
        slot: e.tabBarExtraContent
      }) : e["tabBarExtraContent.left"] || e["tabBarExtraContent.right"] ? {
        left: e["tabBarExtraContent.left"] ? /* @__PURE__ */ x.jsx(E, {
          slot: e["tabBarExtraContent.left"]
        }) : void 0,
        right: e["tabBarExtraContent.right"] ? /* @__PURE__ */ x.jsx(E, {
          slot: e["tabBarExtraContent.right"]
        }) : void 0
      } : c.tabBarExtraContent,
      addIcon: e.addIcon ? /* @__PURE__ */ x.jsx(E, {
        slot: e.addIcon
      }) : c.addIcon,
      removeIcon: e.removeIcon ? /* @__PURE__ */ x.jsx(E, {
        slot: e.removeIcon
      }) : c.removeIcon,
      onChange: (C) => {
        i == null || i(C);
      }
    })]
  });
}));
export {
  pt as Tabs,
  pt as default
};
