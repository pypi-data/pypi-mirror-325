import { i as me, a as M, r as he, g as _e, w as S, b as ge } from "./Index-BKkt-_0U.js";
const R = window.ms_globals.React, ae = window.ms_globals.React.forwardRef, ue = window.ms_globals.React.useRef, de = window.ms_globals.React.useState, fe = window.ms_globals.React.useEffect, te = window.ms_globals.React.useMemo, A = window.ms_globals.ReactDOM.createPortal, we = window.ms_globals.internalContext.useContextPropsContext, F = window.ms_globals.internalContext.ContextPropsProvider, z = window.ms_globals.antd.Tree, pe = window.ms_globals.createItemsContext.createItemsContext;
var be = /\s/;
function ye(e) {
  for (var t = e.length; t-- && be.test(e.charAt(t)); )
    ;
  return t;
}
var ve = /^\s+/;
function xe(e) {
  return e && e.slice(0, ye(e) + 1).replace(ve, "");
}
var G = NaN, Ie = /^[-+]0x[0-9a-f]+$/i, Ce = /^0b[01]+$/i, Ee = /^0o[0-7]+$/i, Re = parseInt;
function q(e) {
  if (typeof e == "number")
    return e;
  if (me(e))
    return G;
  if (M(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = M(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = xe(e);
  var o = Ce.test(e);
  return o || Ee.test(e) ? Re(e.slice(2), o ? 2 : 8) : Ie.test(e) ? G : +e;
}
var D = function() {
  return he.Date.now();
}, Te = "Expected a function", Oe = Math.max, ke = Math.min;
function Le(e, t, o) {
  var s, i, n, r, l, u, p = 0, m = !1, c = !1, w = !0;
  if (typeof e != "function")
    throw new TypeError(Te);
  t = q(t) || 0, M(o) && (m = !!o.leading, c = "maxWait" in o, n = c ? Oe(q(o.maxWait) || 0, t) : n, w = "trailing" in o ? !!o.trailing : w);
  function a(g) {
    var b = s, x = i;
    return s = i = void 0, p = g, r = e.apply(x, b), r;
  }
  function y(g) {
    return p = g, l = setTimeout(_, t), m ? a(g) : r;
  }
  function f(g) {
    var b = g - u, x = g - p, H = t - b;
    return c ? ke(H, n - x) : H;
  }
  function h(g) {
    var b = g - u, x = g - p;
    return u === void 0 || b >= t || b < 0 || c && x >= n;
  }
  function _() {
    var g = D();
    if (h(g))
      return I(g);
    l = setTimeout(_, f(g));
  }
  function I(g) {
    return l = void 0, w && s ? a(g) : (s = i = void 0, r);
  }
  function E() {
    l !== void 0 && clearTimeout(l), p = 0, s = u = i = l = void 0;
  }
  function d() {
    return l === void 0 ? r : I(D());
  }
  function C() {
    var g = D(), b = h(g);
    if (s = arguments, i = this, u = g, b) {
      if (l === void 0)
        return y(u);
      if (c)
        return clearTimeout(l), l = setTimeout(_, t), a(u);
    }
    return l === void 0 && (l = setTimeout(_, t)), r;
  }
  return C.cancel = E, C.flush = d, C;
}
var ne = {
  exports: {}
}, N = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var Se = R, je = Symbol.for("react.element"), Pe = Symbol.for("react.fragment"), Fe = Object.prototype.hasOwnProperty, Ne = Se.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, De = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function re(e, t, o) {
  var s, i = {}, n = null, r = null;
  o !== void 0 && (n = "" + o), t.key !== void 0 && (n = "" + t.key), t.ref !== void 0 && (r = t.ref);
  for (s in t) Fe.call(t, s) && !De.hasOwnProperty(s) && (i[s] = t[s]);
  if (e && e.defaultProps) for (s in t = e.defaultProps, t) i[s] === void 0 && (i[s] = t[s]);
  return {
    $$typeof: je,
    type: e,
    key: n,
    ref: r,
    props: i,
    _owner: Ne.current
  };
}
N.Fragment = Pe;
N.jsx = re;
N.jsxs = re;
ne.exports = N;
var v = ne.exports;
const {
  SvelteComponent: We,
  assign: V,
  binding_callbacks: J,
  check_outros: Ae,
  children: oe,
  claim_element: ie,
  claim_space: Me,
  component_subscribe: X,
  compute_slots: Ue,
  create_slot: Be,
  detach: T,
  element: se,
  empty: Y,
  exclude_internal_props: K,
  get_all_dirty_from_scope: He,
  get_slot_changes: ze,
  group_outros: Ge,
  init: qe,
  insert_hydration: j,
  safe_not_equal: Ve,
  set_custom_element_data: le,
  space: Je,
  transition_in: P,
  transition_out: U,
  update_slot_base: Xe
} = window.__gradio__svelte__internal, {
  beforeUpdate: Ye,
  getContext: Ke,
  onDestroy: Qe,
  setContext: Ze
} = window.__gradio__svelte__internal;
function Q(e) {
  let t, o;
  const s = (
    /*#slots*/
    e[7].default
  ), i = Be(
    s,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = se("svelte-slot"), i && i.c(), this.h();
    },
    l(n) {
      t = ie(n, "SVELTE-SLOT", {
        class: !0
      });
      var r = oe(t);
      i && i.l(r), r.forEach(T), this.h();
    },
    h() {
      le(t, "class", "svelte-1rt0kpf");
    },
    m(n, r) {
      j(n, t, r), i && i.m(t, null), e[9](t), o = !0;
    },
    p(n, r) {
      i && i.p && (!o || r & /*$$scope*/
      64) && Xe(
        i,
        s,
        n,
        /*$$scope*/
        n[6],
        o ? ze(
          s,
          /*$$scope*/
          n[6],
          r,
          null
        ) : He(
          /*$$scope*/
          n[6]
        ),
        null
      );
    },
    i(n) {
      o || (P(i, n), o = !0);
    },
    o(n) {
      U(i, n), o = !1;
    },
    d(n) {
      n && T(t), i && i.d(n), e[9](null);
    }
  };
}
function $e(e) {
  let t, o, s, i, n = (
    /*$$slots*/
    e[4].default && Q(e)
  );
  return {
    c() {
      t = se("react-portal-target"), o = Je(), n && n.c(), s = Y(), this.h();
    },
    l(r) {
      t = ie(r, "REACT-PORTAL-TARGET", {
        class: !0
      }), oe(t).forEach(T), o = Me(r), n && n.l(r), s = Y(), this.h();
    },
    h() {
      le(t, "class", "svelte-1rt0kpf");
    },
    m(r, l) {
      j(r, t, l), e[8](t), j(r, o, l), n && n.m(r, l), j(r, s, l), i = !0;
    },
    p(r, [l]) {
      /*$$slots*/
      r[4].default ? n ? (n.p(r, l), l & /*$$slots*/
      16 && P(n, 1)) : (n = Q(r), n.c(), P(n, 1), n.m(s.parentNode, s)) : n && (Ge(), U(n, 1, 1, () => {
        n = null;
      }), Ae());
    },
    i(r) {
      i || (P(n), i = !0);
    },
    o(r) {
      U(n), i = !1;
    },
    d(r) {
      r && (T(t), T(o), T(s)), e[8](null), n && n.d(r);
    }
  };
}
function Z(e) {
  const {
    svelteInit: t,
    ...o
  } = e;
  return o;
}
function et(e, t, o) {
  let s, i, {
    $$slots: n = {},
    $$scope: r
  } = t;
  const l = Ue(n);
  let {
    svelteInit: u
  } = t;
  const p = S(Z(t)), m = S();
  X(e, m, (d) => o(0, s = d));
  const c = S();
  X(e, c, (d) => o(1, i = d));
  const w = [], a = Ke("$$ms-gr-react-wrapper"), {
    slotKey: y,
    slotIndex: f,
    subSlotIndex: h
  } = _e() || {}, _ = u({
    parent: a,
    props: p,
    target: m,
    slot: c,
    slotKey: y,
    slotIndex: f,
    subSlotIndex: h,
    onDestroy(d) {
      w.push(d);
    }
  });
  Ze("$$ms-gr-react-wrapper", _), Ye(() => {
    p.set(Z(t));
  }), Qe(() => {
    w.forEach((d) => d());
  });
  function I(d) {
    J[d ? "unshift" : "push"](() => {
      s = d, m.set(s);
    });
  }
  function E(d) {
    J[d ? "unshift" : "push"](() => {
      i = d, c.set(i);
    });
  }
  return e.$$set = (d) => {
    o(17, t = V(V({}, t), K(d))), "svelteInit" in d && o(5, u = d.svelteInit), "$$scope" in d && o(6, r = d.$$scope);
  }, t = K(t), [s, i, m, c, l, u, r, n, I, E];
}
class tt extends We {
  constructor(t) {
    super(), qe(this, t, et, $e, Ve, {
      svelteInit: 5
    });
  }
}
const $ = window.ms_globals.rerender, W = window.ms_globals.tree;
function nt(e, t = {}) {
  function o(s) {
    const i = S(), n = new tt({
      ...s,
      props: {
        svelteInit(r) {
          window.ms_globals.autokey += 1;
          const l = {
            key: window.ms_globals.autokey,
            svelteInstance: i,
            reactComponent: e,
            props: r.props,
            slot: r.slot,
            target: r.target,
            slotIndex: r.slotIndex,
            subSlotIndex: r.subSlotIndex,
            ignore: t.ignore,
            slotKey: r.slotKey,
            nodes: []
          }, u = r.parent ?? W;
          return u.nodes = [...u.nodes, l], $({
            createPortal: A,
            node: W
          }), r.onDestroy(() => {
            u.nodes = u.nodes.filter((p) => p.svelteInstance !== i), $({
              createPortal: A,
              node: W
            });
          }), l;
        },
        ...s.props
      }
    });
    return i.set(n), n;
  }
  return new Promise((s) => {
    window.ms_globals.initializePromise.then(() => {
      s(o);
    });
  });
}
const rt = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function ot(e) {
  return e ? Object.keys(e).reduce((t, o) => {
    const s = e[o];
    return t[o] = it(o, s), t;
  }, {}) : {};
}
function it(e, t) {
  return typeof t == "number" && !rt.includes(e) ? t + "px" : t;
}
function B(e) {
  const t = [], o = e.cloneNode(!1);
  if (e._reactElement) {
    const i = R.Children.toArray(e._reactElement.props.children).map((n) => {
      if (R.isValidElement(n) && n.props.__slot__) {
        const {
          portals: r,
          clonedElement: l
        } = B(n.props.el);
        return R.cloneElement(n, {
          ...n.props,
          el: l,
          children: [...R.Children.toArray(n.props.children), ...r]
        });
      }
      return null;
    });
    return i.originalChildren = e._reactElement.props.children, t.push(A(R.cloneElement(e._reactElement, {
      ...e._reactElement.props,
      children: i
    }), o)), {
      clonedElement: o,
      portals: t
    };
  }
  Object.keys(e.getEventListeners()).forEach((i) => {
    e.getEventListeners(i).forEach(({
      listener: r,
      type: l,
      useCapture: u
    }) => {
      o.addEventListener(l, r, u);
    });
  });
  const s = Array.from(e.childNodes);
  for (let i = 0; i < s.length; i++) {
    const n = s[i];
    if (n.nodeType === 1) {
      const {
        clonedElement: r,
        portals: l
      } = B(n);
      t.push(...l), o.appendChild(r);
    } else n.nodeType === 3 && o.appendChild(n.cloneNode());
  }
  return {
    clonedElement: o,
    portals: t
  };
}
function st(e, t) {
  e && (typeof e == "function" ? e(t) : e.current = t);
}
const k = ae(({
  slot: e,
  clone: t,
  className: o,
  style: s,
  observeAttributes: i
}, n) => {
  const r = ue(), [l, u] = de([]), {
    forceClone: p
  } = we(), m = p ? !0 : t;
  return fe(() => {
    var y;
    if (!r.current || !e)
      return;
    let c = e;
    function w() {
      let f = c;
      if (c.tagName.toLowerCase() === "svelte-slot" && c.children.length === 1 && c.children[0] && (f = c.children[0], f.tagName.toLowerCase() === "react-portal-target" && f.children[0] && (f = f.children[0])), st(n, f), o && f.classList.add(...o.split(" ")), s) {
        const h = ot(s);
        Object.keys(h).forEach((_) => {
          f.style[_] = h[_];
        });
      }
    }
    let a = null;
    if (m && window.MutationObserver) {
      let f = function() {
        var E, d, C;
        (E = r.current) != null && E.contains(c) && ((d = r.current) == null || d.removeChild(c));
        const {
          portals: _,
          clonedElement: I
        } = B(e);
        c = I, u(_), c.style.display = "contents", w(), (C = r.current) == null || C.appendChild(c);
      };
      f();
      const h = Le(() => {
        f(), a == null || a.disconnect(), a == null || a.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: i
        });
      }, 50);
      a = new window.MutationObserver(h), a.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      c.style.display = "contents", w(), (y = r.current) == null || y.appendChild(c);
    return () => {
      var f, h;
      c.style.display = "", (f = r.current) != null && f.contains(c) && ((h = r.current) == null || h.removeChild(c)), a == null || a.disconnect();
    };
  }, [e, m, o, s, n, i]), R.createElement("react-child", {
    ref: r,
    style: {
      display: "contents"
    }
  }, ...l);
});
function lt(e) {
  return /^(?:async\s+)?(?:function\s*(?:\w*\s*)?\(|\([\w\s,=]*\)\s*=>|\(\{[\w\s,=]*\}\)\s*=>|function\s*\*\s*\w*\s*\()/i.test(e.trim());
}
function ct(e, t = !1) {
  try {
    if (ge(e))
      return e;
    if (t && !lt(e))
      return;
    if (typeof e == "string") {
      let o = e.trim();
      return o.startsWith(";") && (o = o.slice(1)), o.endsWith(";") && (o = o.slice(0, -1)), new Function(`return (...args) => (${o})(...args)`)();
    }
    return;
  } catch {
    return;
  }
}
function O(e, t) {
  return te(() => ct(e, t), [e, t]);
}
function at(e) {
  return Object.keys(e).reduce((t, o) => (e[o] !== void 0 && (t[o] = e[o]), t), {});
}
function ce(e, t, o) {
  const s = e.filter(Boolean);
  if (s.length !== 0)
    return s.map((i, n) => {
      var p;
      if (typeof i != "object")
        return t != null && t.fallback ? t.fallback(i) : i;
      const r = {
        ...i.props,
        key: ((p = i.props) == null ? void 0 : p.key) ?? (o ? `${o}-${n}` : `${n}`)
      };
      let l = r;
      Object.keys(i.slots).forEach((m) => {
        if (!i.slots[m] || !(i.slots[m] instanceof Element) && !i.slots[m].el)
          return;
        const c = m.split(".");
        c.forEach((_, I) => {
          l[_] || (l[_] = {}), I !== c.length - 1 && (l = r[_]);
        });
        const w = i.slots[m];
        let a, y, f = (t == null ? void 0 : t.clone) ?? !1, h = t == null ? void 0 : t.forceClone;
        w instanceof Element ? a = w : (a = w.el, y = w.callback, f = w.clone ?? f, h = w.forceClone ?? h), h = h ?? !!y, l[c[c.length - 1]] = a ? y ? (..._) => (y(c[c.length - 1], _), /* @__PURE__ */ v.jsx(F, {
          params: _,
          forceClone: h,
          children: /* @__PURE__ */ v.jsx(k, {
            slot: a,
            clone: f
          })
        })) : /* @__PURE__ */ v.jsx(F, {
          forceClone: h,
          children: /* @__PURE__ */ v.jsx(k, {
            slot: a,
            clone: f
          })
        }) : l[c[c.length - 1]], l = r;
      });
      const u = (t == null ? void 0 : t.children) || "children";
      return i[u] ? r[u] = ce(i[u], t, `${n}`) : t != null && t.children && (r[u] = void 0, Reflect.deleteProperty(r, u)), r;
    });
}
function ee(e, t) {
  return e ? /* @__PURE__ */ v.jsx(k, {
    slot: e,
    clone: t == null ? void 0 : t.clone
  }) : null;
}
function L({
  key: e,
  slots: t,
  targets: o
}, s) {
  return t[e] ? (...i) => o ? o.map((n, r) => /* @__PURE__ */ v.jsx(F, {
    params: i,
    forceClone: !0,
    children: ee(n, {
      clone: !0,
      ...s
    })
  }, r)) : /* @__PURE__ */ v.jsx(F, {
    params: i,
    forceClone: !0,
    children: ee(t[e], {
      clone: !0,
      ...s
    })
  }) : void 0;
}
const {
  withItemsContextProvider: ut,
  useItems: dt,
  ItemHandler: mt
} = pe("antd-tree-tree-nodes"), ht = nt(ut(["default", "treeData"], ({
  slots: e,
  filterTreeNode: t,
  treeData: o,
  draggable: s,
  allowDrop: i,
  onCheck: n,
  onSelect: r,
  onExpand: l,
  children: u,
  directory: p,
  setSlotParams: m,
  onLoadData: c,
  titleRender: w,
  ...a
}) => {
  const y = O(t), f = O(s), h = O(w), _ = O(typeof s == "object" ? s.nodeDraggable : void 0), I = O(i), E = p ? z.DirectoryTree : z, {
    items: d
  } = dt(), C = d.treeData.length > 0 ? d.treeData : d.default, g = te(() => ({
    ...a,
    treeData: o || ce(C, {
      clone: !0
    }),
    showLine: e["showLine.showLeafIcon"] ? {
      showLeafIcon: L({
        slots: e,
        setSlotParams: m,
        key: "showLine.showLeafIcon"
      })
    } : a.showLine,
    icon: e.icon ? L({
      slots: e,
      setSlotParams: m,
      key: "icon"
    }) : a.icon,
    switcherLoadingIcon: e.switcherLoadingIcon ? /* @__PURE__ */ v.jsx(k, {
      slot: e.switcherLoadingIcon
    }) : a.switcherLoadingIcon,
    switcherIcon: e.switcherIcon ? L({
      slots: e,
      setSlotParams: m,
      key: "switcherIcon"
    }) : a.switcherIcon,
    titleRender: e.titleRender ? L({
      slots: e,
      setSlotParams: m,
      key: "titleRender"
    }) : h,
    draggable: e["draggable.icon"] || _ ? {
      icon: e["draggable.icon"] ? /* @__PURE__ */ v.jsx(k, {
        slot: e["draggable.icon"]
      }) : typeof s == "object" ? s.icon : void 0,
      nodeDraggable: _
    } : f || s,
    loadData: c
  }), [a, o, C, e, m, _, s, h, f, c]);
  return /* @__PURE__ */ v.jsxs(v.Fragment, {
    children: [/* @__PURE__ */ v.jsx("div", {
      style: {
        display: "none"
      },
      children: u
    }), /* @__PURE__ */ v.jsx(E, {
      ...at(g),
      filterTreeNode: y,
      allowDrop: I,
      onSelect: (b, ...x) => {
        r == null || r(b, ...x);
      },
      onExpand: (b, ...x) => {
        l == null || l(b, ...x);
      },
      onCheck: (b, ...x) => {
        n == null || n(b, ...x);
      }
    })]
  });
}));
export {
  ht as Tree,
  ht as default
};
