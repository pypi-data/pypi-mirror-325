import { i as fe, a as A, r as me, g as _e, w as k, b as he } from "./Index-COaPcUnO.js";
const v = window.ms_globals.React, ce = window.ms_globals.React.forwardRef, ae = window.ms_globals.React.useRef, ue = window.ms_globals.React.useState, de = window.ms_globals.React.useEffect, ee = window.ms_globals.React.useMemo, W = window.ms_globals.ReactDOM.createPortal, ge = window.ms_globals.internalContext.useContextPropsContext, T = window.ms_globals.internalContext.ContextPropsProvider, pe = window.ms_globals.antd.Dropdown, we = window.ms_globals.createItemsContext.createItemsContext;
var be = /\s/;
function xe(t) {
  for (var e = t.length; e-- && be.test(t.charAt(e)); )
    ;
  return e;
}
var ye = /^\s+/;
function Ce(t) {
  return t && t.slice(0, xe(t) + 1).replace(ye, "");
}
var B = NaN, ve = /^[-+]0x[0-9a-f]+$/i, Ee = /^0b[01]+$/i, Ie = /^0o[0-7]+$/i, Re = parseInt;
function H(t) {
  if (typeof t == "number")
    return t;
  if (fe(t))
    return B;
  if (A(t)) {
    var e = typeof t.valueOf == "function" ? t.valueOf() : t;
    t = A(e) ? e + "" : e;
  }
  if (typeof t != "string")
    return t === 0 ? t : +t;
  t = Ce(t);
  var l = Ee.test(t);
  return l || Ie.test(t) ? Re(t.slice(2), l ? 2 : 8) : ve.test(t) ? B : +t;
}
var N = function() {
  return me.Date.now();
}, Se = "Expected a function", ke = Math.max, Oe = Math.min;
function Pe(t, e, l) {
  var s, o, r, n, i, a, p = 0, m = !1, c = !1, _ = !0;
  if (typeof t != "function")
    throw new TypeError(Se);
  e = H(e) || 0, A(l) && (m = !!l.leading, c = "maxWait" in l, r = c ? ke(H(l.maxWait) || 0, e) : r, _ = "trailing" in l ? !!l.trailing : _);
  function u(g) {
    var C = s, S = o;
    return s = o = void 0, p = g, n = t.apply(S, C), n;
  }
  function x(g) {
    return p = g, i = setTimeout(w, e), m ? u(g) : n;
  }
  function f(g) {
    var C = g - a, S = g - p, U = e - C;
    return c ? Oe(U, r - S) : U;
  }
  function h(g) {
    var C = g - a, S = g - p;
    return a === void 0 || C >= e || C < 0 || c && S >= r;
  }
  function w() {
    var g = N();
    if (h(g))
      return y(g);
    i = setTimeout(w, f(g));
  }
  function y(g) {
    return i = void 0, _ && s ? u(g) : (s = o = void 0, n);
  }
  function E() {
    i !== void 0 && clearTimeout(i), p = 0, s = a = o = i = void 0;
  }
  function d() {
    return i === void 0 ? n : y(N());
  }
  function I() {
    var g = N(), C = h(g);
    if (s = arguments, o = this, a = g, C) {
      if (i === void 0)
        return x(a);
      if (c)
        return clearTimeout(i), i = setTimeout(w, e), u(a);
    }
    return i === void 0 && (i = setTimeout(w, e)), n;
  }
  return I.cancel = E, I.flush = d, I;
}
var te = {
  exports: {}
}, L = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var Te = v, je = Symbol.for("react.element"), Le = Symbol.for("react.fragment"), Ne = Object.prototype.hasOwnProperty, Fe = Te.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, We = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function ne(t, e, l) {
  var s, o = {}, r = null, n = null;
  l !== void 0 && (r = "" + l), e.key !== void 0 && (r = "" + e.key), e.ref !== void 0 && (n = e.ref);
  for (s in e) Ne.call(e, s) && !We.hasOwnProperty(s) && (o[s] = e[s]);
  if (t && t.defaultProps) for (s in e = t.defaultProps, e) o[s] === void 0 && (o[s] = e[s]);
  return {
    $$typeof: je,
    type: t,
    key: r,
    ref: n,
    props: o,
    _owner: Fe.current
  };
}
L.Fragment = Le;
L.jsx = ne;
L.jsxs = ne;
te.exports = L;
var b = te.exports;
const {
  SvelteComponent: Ae,
  assign: z,
  binding_callbacks: G,
  check_outros: De,
  children: re,
  claim_element: oe,
  claim_space: Me,
  component_subscribe: q,
  compute_slots: Ue,
  create_slot: Be,
  detach: R,
  element: le,
  empty: V,
  exclude_internal_props: J,
  get_all_dirty_from_scope: He,
  get_slot_changes: ze,
  group_outros: Ge,
  init: qe,
  insert_hydration: O,
  safe_not_equal: Ve,
  set_custom_element_data: se,
  space: Je,
  transition_in: P,
  transition_out: D,
  update_slot_base: Xe
} = window.__gradio__svelte__internal, {
  beforeUpdate: Ye,
  getContext: Ke,
  onDestroy: Qe,
  setContext: Ze
} = window.__gradio__svelte__internal;
function X(t) {
  let e, l;
  const s = (
    /*#slots*/
    t[7].default
  ), o = Be(
    s,
    t,
    /*$$scope*/
    t[6],
    null
  );
  return {
    c() {
      e = le("svelte-slot"), o && o.c(), this.h();
    },
    l(r) {
      e = oe(r, "SVELTE-SLOT", {
        class: !0
      });
      var n = re(e);
      o && o.l(n), n.forEach(R), this.h();
    },
    h() {
      se(e, "class", "svelte-1rt0kpf");
    },
    m(r, n) {
      O(r, e, n), o && o.m(e, null), t[9](e), l = !0;
    },
    p(r, n) {
      o && o.p && (!l || n & /*$$scope*/
      64) && Xe(
        o,
        s,
        r,
        /*$$scope*/
        r[6],
        l ? ze(
          s,
          /*$$scope*/
          r[6],
          n,
          null
        ) : He(
          /*$$scope*/
          r[6]
        ),
        null
      );
    },
    i(r) {
      l || (P(o, r), l = !0);
    },
    o(r) {
      D(o, r), l = !1;
    },
    d(r) {
      r && R(e), o && o.d(r), t[9](null);
    }
  };
}
function $e(t) {
  let e, l, s, o, r = (
    /*$$slots*/
    t[4].default && X(t)
  );
  return {
    c() {
      e = le("react-portal-target"), l = Je(), r && r.c(), s = V(), this.h();
    },
    l(n) {
      e = oe(n, "REACT-PORTAL-TARGET", {
        class: !0
      }), re(e).forEach(R), l = Me(n), r && r.l(n), s = V(), this.h();
    },
    h() {
      se(e, "class", "svelte-1rt0kpf");
    },
    m(n, i) {
      O(n, e, i), t[8](e), O(n, l, i), r && r.m(n, i), O(n, s, i), o = !0;
    },
    p(n, [i]) {
      /*$$slots*/
      n[4].default ? r ? (r.p(n, i), i & /*$$slots*/
      16 && P(r, 1)) : (r = X(n), r.c(), P(r, 1), r.m(s.parentNode, s)) : r && (Ge(), D(r, 1, 1, () => {
        r = null;
      }), De());
    },
    i(n) {
      o || (P(r), o = !0);
    },
    o(n) {
      D(r), o = !1;
    },
    d(n) {
      n && (R(e), R(l), R(s)), t[8](null), r && r.d(n);
    }
  };
}
function Y(t) {
  const {
    svelteInit: e,
    ...l
  } = t;
  return l;
}
function et(t, e, l) {
  let s, o, {
    $$slots: r = {},
    $$scope: n
  } = e;
  const i = Ue(r);
  let {
    svelteInit: a
  } = e;
  const p = k(Y(e)), m = k();
  q(t, m, (d) => l(0, s = d));
  const c = k();
  q(t, c, (d) => l(1, o = d));
  const _ = [], u = Ke("$$ms-gr-react-wrapper"), {
    slotKey: x,
    slotIndex: f,
    subSlotIndex: h
  } = _e() || {}, w = a({
    parent: u,
    props: p,
    target: m,
    slot: c,
    slotKey: x,
    slotIndex: f,
    subSlotIndex: h,
    onDestroy(d) {
      _.push(d);
    }
  });
  Ze("$$ms-gr-react-wrapper", w), Ye(() => {
    p.set(Y(e));
  }), Qe(() => {
    _.forEach((d) => d());
  });
  function y(d) {
    G[d ? "unshift" : "push"](() => {
      s = d, m.set(s);
    });
  }
  function E(d) {
    G[d ? "unshift" : "push"](() => {
      o = d, c.set(o);
    });
  }
  return t.$$set = (d) => {
    l(17, e = z(z({}, e), J(d))), "svelteInit" in d && l(5, a = d.svelteInit), "$$scope" in d && l(6, n = d.$$scope);
  }, e = J(e), [s, o, m, c, i, a, n, r, y, E];
}
class tt extends Ae {
  constructor(e) {
    super(), qe(this, e, et, $e, Ve, {
      svelteInit: 5
    });
  }
}
const K = window.ms_globals.rerender, F = window.ms_globals.tree;
function nt(t, e = {}) {
  function l(s) {
    const o = k(), r = new tt({
      ...s,
      props: {
        svelteInit(n) {
          window.ms_globals.autokey += 1;
          const i = {
            key: window.ms_globals.autokey,
            svelteInstance: o,
            reactComponent: t,
            props: n.props,
            slot: n.slot,
            target: n.target,
            slotIndex: n.slotIndex,
            subSlotIndex: n.subSlotIndex,
            ignore: e.ignore,
            slotKey: n.slotKey,
            nodes: []
          }, a = n.parent ?? F;
          return a.nodes = [...a.nodes, i], K({
            createPortal: W,
            node: F
          }), n.onDestroy(() => {
            a.nodes = a.nodes.filter((p) => p.svelteInstance !== o), K({
              createPortal: W,
              node: F
            });
          }), i;
        },
        ...s.props
      }
    });
    return o.set(r), r;
  }
  return new Promise((s) => {
    window.ms_globals.initializePromise.then(() => {
      s(l);
    });
  });
}
const rt = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function ot(t) {
  return t ? Object.keys(t).reduce((e, l) => {
    const s = t[l];
    return e[l] = lt(l, s), e;
  }, {}) : {};
}
function lt(t, e) {
  return typeof e == "number" && !rt.includes(t) ? e + "px" : e;
}
function M(t) {
  const e = [], l = t.cloneNode(!1);
  if (t._reactElement) {
    const o = v.Children.toArray(t._reactElement.props.children).map((r) => {
      if (v.isValidElement(r) && r.props.__slot__) {
        const {
          portals: n,
          clonedElement: i
        } = M(r.props.el);
        return v.cloneElement(r, {
          ...r.props,
          el: i,
          children: [...v.Children.toArray(r.props.children), ...n]
        });
      }
      return null;
    });
    return o.originalChildren = t._reactElement.props.children, e.push(W(v.cloneElement(t._reactElement, {
      ...t._reactElement.props,
      children: o
    }), l)), {
      clonedElement: l,
      portals: e
    };
  }
  Object.keys(t.getEventListeners()).forEach((o) => {
    t.getEventListeners(o).forEach(({
      listener: n,
      type: i,
      useCapture: a
    }) => {
      l.addEventListener(i, n, a);
    });
  });
  const s = Array.from(t.childNodes);
  for (let o = 0; o < s.length; o++) {
    const r = s[o];
    if (r.nodeType === 1) {
      const {
        clonedElement: n,
        portals: i
      } = M(r);
      e.push(...i), l.appendChild(n);
    } else r.nodeType === 3 && l.appendChild(r.cloneNode());
  }
  return {
    clonedElement: l,
    portals: e
  };
}
function st(t, e) {
  t && (typeof t == "function" ? t(e) : t.current = e);
}
const j = ce(({
  slot: t,
  clone: e,
  className: l,
  style: s,
  observeAttributes: o
}, r) => {
  const n = ae(), [i, a] = ue([]), {
    forceClone: p
  } = ge(), m = p ? !0 : e;
  return de(() => {
    var x;
    if (!n.current || !t)
      return;
    let c = t;
    function _() {
      let f = c;
      if (c.tagName.toLowerCase() === "svelte-slot" && c.children.length === 1 && c.children[0] && (f = c.children[0], f.tagName.toLowerCase() === "react-portal-target" && f.children[0] && (f = f.children[0])), st(r, f), l && f.classList.add(...l.split(" ")), s) {
        const h = ot(s);
        Object.keys(h).forEach((w) => {
          f.style[w] = h[w];
        });
      }
    }
    let u = null;
    if (m && window.MutationObserver) {
      let f = function() {
        var E, d, I;
        (E = n.current) != null && E.contains(c) && ((d = n.current) == null || d.removeChild(c));
        const {
          portals: w,
          clonedElement: y
        } = M(t);
        c = y, a(w), c.style.display = "contents", _(), (I = n.current) == null || I.appendChild(c);
      };
      f();
      const h = Pe(() => {
        f(), u == null || u.disconnect(), u == null || u.observe(t, {
          childList: !0,
          subtree: !0,
          attributes: o
        });
      }, 50);
      u = new window.MutationObserver(h), u.observe(t, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      c.style.display = "contents", _(), (x = n.current) == null || x.appendChild(c);
    return () => {
      var f, h;
      c.style.display = "", (f = n.current) != null && f.contains(c) && ((h = n.current) == null || h.removeChild(c)), u == null || u.disconnect();
    };
  }, [t, m, l, s, r, o]), v.createElement("react-child", {
    ref: n,
    style: {
      display: "contents"
    }
  }, ...i);
});
function it(t) {
  return /^(?:async\s+)?(?:function\s*(?:\w*\s*)?\(|\([\w\s,=]*\)\s*=>|\(\{[\w\s,=]*\}\)\s*=>|function\s*\*\s*\w*\s*\()/i.test(t.trim());
}
function ct(t, e = !1) {
  try {
    if (he(t))
      return t;
    if (e && !it(t))
      return;
    if (typeof t == "string") {
      let l = t.trim();
      return l.startsWith(";") && (l = l.slice(1)), l.endsWith(";") && (l = l.slice(0, -1)), new Function(`return (...args) => (${l})(...args)`)();
    }
    return;
  } catch {
    return;
  }
}
function Q(t, e) {
  return ee(() => ct(t, e), [t, e]);
}
function ie(t, e, l) {
  const s = t.filter(Boolean);
  if (s.length !== 0)
    return s.map((o, r) => {
      var p;
      if (typeof o != "object")
        return e != null && e.fallback ? e.fallback(o) : o;
      const n = {
        ...o.props,
        key: ((p = o.props) == null ? void 0 : p.key) ?? (l ? `${l}-${r}` : `${r}`)
      };
      let i = n;
      Object.keys(o.slots).forEach((m) => {
        if (!o.slots[m] || !(o.slots[m] instanceof Element) && !o.slots[m].el)
          return;
        const c = m.split(".");
        c.forEach((w, y) => {
          i[w] || (i[w] = {}), y !== c.length - 1 && (i = n[w]);
        });
        const _ = o.slots[m];
        let u, x, f = (e == null ? void 0 : e.clone) ?? !1, h = e == null ? void 0 : e.forceClone;
        _ instanceof Element ? u = _ : (u = _.el, x = _.callback, f = _.clone ?? f, h = _.forceClone ?? h), h = h ?? !!x, i[c[c.length - 1]] = u ? x ? (...w) => (x(c[c.length - 1], w), /* @__PURE__ */ b.jsx(T, {
          params: w,
          forceClone: h,
          children: /* @__PURE__ */ b.jsx(j, {
            slot: u,
            clone: f
          })
        })) : /* @__PURE__ */ b.jsx(T, {
          forceClone: h,
          children: /* @__PURE__ */ b.jsx(j, {
            slot: u,
            clone: f
          })
        }) : i[c[c.length - 1]], i = n;
      });
      const a = (e == null ? void 0 : e.children) || "children";
      return o[a] ? n[a] = ie(o[a], e, `${r}`) : e != null && e.children && (n[a] = void 0, Reflect.deleteProperty(n, a)), n;
    });
}
function Z(t, e) {
  return t ? /* @__PURE__ */ b.jsx(j, {
    slot: t,
    clone: e == null ? void 0 : e.clone
  }) : null;
}
function $({
  key: t,
  slots: e,
  targets: l
}, s) {
  return e[t] ? (...o) => l ? l.map((r, n) => /* @__PURE__ */ b.jsx(T, {
    params: o,
    forceClone: (s == null ? void 0 : s.forceClone) ?? !0,
    children: Z(r, {
      clone: !0,
      ...s
    })
  }, n)) : /* @__PURE__ */ b.jsx(T, {
    params: o,
    forceClone: (s == null ? void 0 : s.forceClone) ?? !0,
    children: Z(e[t], {
      clone: !0,
      ...s
    })
  }) : void 0;
}
const {
  useItems: at,
  withItemsContextProvider: ut,
  ItemHandler: ft
} = we("antd-menu-items"), mt = nt(ut(["menu.items"], ({
  getPopupContainer: t,
  innerStyle: e,
  children: l,
  slots: s,
  dropdownRender: o,
  setSlotParams: r,
  ...n
}) => {
  var m, c, _;
  const i = Q(t), a = Q(o), {
    items: {
      "menu.items": p
    }
  } = at();
  return /* @__PURE__ */ b.jsx(b.Fragment, {
    children: /* @__PURE__ */ b.jsx(pe, {
      ...n,
      menu: {
        ...n.menu,
        items: ee(() => {
          var u;
          return ((u = n.menu) == null ? void 0 : u.items) || ie(p, {
            clone: !0
          }) || [];
        }, [p, (m = n.menu) == null ? void 0 : m.items]),
        expandIcon: s["menu.expandIcon"] ? $({
          slots: s,
          setSlotParams: r,
          key: "menu.expandIcon"
        }, {
          clone: !0
        }) : (c = n.menu) == null ? void 0 : c.expandIcon,
        overflowedIndicator: s["menu.overflowedIndicator"] ? /* @__PURE__ */ b.jsx(j, {
          slot: s["menu.overflowedIndicator"]
        }) : (_ = n.menu) == null ? void 0 : _.overflowedIndicator
      },
      getPopupContainer: i,
      dropdownRender: s.dropdownRender ? $({
        slots: s,
        setSlotParams: r,
        key: "dropdownRender"
      }, {
        clone: !0
      }) : a,
      children: /* @__PURE__ */ b.jsx("div", {
        className: "ms-gr-antd-dropdown-content",
        style: {
          display: "inline-block",
          ...e
        },
        children: l
      })
    })
  });
}));
export {
  mt as Dropdown,
  mt as default
};
