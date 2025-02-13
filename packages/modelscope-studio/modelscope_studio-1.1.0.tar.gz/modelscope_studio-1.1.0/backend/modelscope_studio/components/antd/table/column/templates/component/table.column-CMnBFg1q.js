import { i as ue, a as W, r as fe, g as me, w as k, c as pe } from "./Index-uuD46UEf.js";
const I = window.ms_globals.React, ie = window.ms_globals.React.forwardRef, ce = window.ms_globals.React.useRef, ae = window.ms_globals.React.useState, de = window.ms_globals.React.useEffect, A = window.ms_globals.ReactDOM.createPortal, he = window.ms_globals.internalContext.useContextPropsContext, D = window.ms_globals.internalContext.ContextPropsProvider, S = window.ms_globals.createItemsContext.createItemsContext;
var _e = /\s/;
function we(t) {
  for (var e = t.length; e-- && _e.test(t.charAt(e)); )
    ;
  return e;
}
var ge = /^\s+/;
function be(t) {
  return t && t.slice(0, we(t) + 1).replace(ge, "");
}
var z = NaN, Ce = /^[-+]0x[0-9a-f]+$/i, xe = /^0b[01]+$/i, ve = /^0o[0-7]+$/i, Ie = parseInt;
function G(t) {
  if (typeof t == "number")
    return t;
  if (ue(t))
    return z;
  if (W(t)) {
    var e = typeof t.valueOf == "function" ? t.valueOf() : t;
    t = W(e) ? e + "" : e;
  }
  if (typeof t != "string")
    return t === 0 ? t : +t;
  t = be(t);
  var s = xe.test(t);
  return s || ve.test(t) ? Ie(t.slice(2), s ? 2 : 8) : Ce.test(t) ? z : +t;
}
var L = function() {
  return fe.Date.now();
}, Ee = "Expected a function", ye = Math.max, Pe = Math.min;
function Re(t, e, s) {
  var l, o, n, r, i, a, w = 0, m = !1, c = !1, p = !0;
  if (typeof t != "function")
    throw new TypeError(Ee);
  e = G(e) || 0, W(s) && (m = !!s.leading, c = "maxWait" in s, n = c ? ye(G(s.maxWait) || 0, e) : n, p = "trailing" in s ? !!s.trailing : p);
  function d(_) {
    var x = l, R = o;
    return l = o = void 0, w = _, r = t.apply(R, x), r;
  }
  function b(_) {
    return w = _, i = setTimeout(g, e), m ? d(_) : r;
  }
  function f(_) {
    var x = _ - a, R = _ - w, U = e - x;
    return c ? Pe(U, n - R) : U;
  }
  function h(_) {
    var x = _ - a, R = _ - w;
    return a === void 0 || x >= e || x < 0 || c && R >= n;
  }
  function g() {
    var _ = L();
    if (h(_))
      return C(_);
    i = setTimeout(g, f(_));
  }
  function C(_) {
    return i = void 0, p && l ? d(_) : (l = o = void 0, r);
  }
  function E() {
    i !== void 0 && clearTimeout(i), w = 0, l = a = o = i = void 0;
  }
  function u() {
    return i === void 0 ? r : C(L());
  }
  function y() {
    var _ = L(), x = h(_);
    if (l = arguments, o = this, a = _, x) {
      if (i === void 0)
        return b(a);
      if (c)
        return clearTimeout(i), i = setTimeout(g, e), d(a);
    }
    return i === void 0 && (i = setTimeout(g, e)), r;
  }
  return y.cancel = E, y.flush = u, y;
}
var ee = {
  exports: {}
}, j = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var Se = I, ke = Symbol.for("react.element"), Oe = Symbol.for("react.fragment"), Te = Object.prototype.hasOwnProperty, De = Se.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, je = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function te(t, e, s) {
  var l, o = {}, n = null, r = null;
  s !== void 0 && (n = "" + s), e.key !== void 0 && (n = "" + e.key), e.ref !== void 0 && (r = e.ref);
  for (l in e) Te.call(e, l) && !je.hasOwnProperty(l) && (o[l] = e[l]);
  if (t && t.defaultProps) for (l in e = t.defaultProps, e) o[l] === void 0 && (o[l] = e[l]);
  return {
    $$typeof: ke,
    type: t,
    key: n,
    ref: r,
    props: o,
    _owner: De.current
  };
}
j.Fragment = Oe;
j.jsx = te;
j.jsxs = te;
ee.exports = j;
var v = ee.exports;
const {
  SvelteComponent: Le,
  assign: q,
  binding_callbacks: V,
  check_outros: Ne,
  children: ne,
  claim_element: re,
  claim_space: Ae,
  component_subscribe: J,
  compute_slots: We,
  create_slot: Me,
  detach: P,
  element: oe,
  empty: X,
  exclude_internal_props: Y,
  get_all_dirty_from_scope: Be,
  get_slot_changes: Fe,
  group_outros: He,
  init: Ue,
  insert_hydration: O,
  safe_not_equal: ze,
  set_custom_element_data: le,
  space: Ge,
  transition_in: T,
  transition_out: M,
  update_slot_base: qe
} = window.__gradio__svelte__internal, {
  beforeUpdate: Ve,
  getContext: Je,
  onDestroy: Xe,
  setContext: Ye
} = window.__gradio__svelte__internal;
function K(t) {
  let e, s;
  const l = (
    /*#slots*/
    t[7].default
  ), o = Me(
    l,
    t,
    /*$$scope*/
    t[6],
    null
  );
  return {
    c() {
      e = oe("svelte-slot"), o && o.c(), this.h();
    },
    l(n) {
      e = re(n, "SVELTE-SLOT", {
        class: !0
      });
      var r = ne(e);
      o && o.l(r), r.forEach(P), this.h();
    },
    h() {
      le(e, "class", "svelte-1rt0kpf");
    },
    m(n, r) {
      O(n, e, r), o && o.m(e, null), t[9](e), s = !0;
    },
    p(n, r) {
      o && o.p && (!s || r & /*$$scope*/
      64) && qe(
        o,
        l,
        n,
        /*$$scope*/
        n[6],
        s ? Fe(
          l,
          /*$$scope*/
          n[6],
          r,
          null
        ) : Be(
          /*$$scope*/
          n[6]
        ),
        null
      );
    },
    i(n) {
      s || (T(o, n), s = !0);
    },
    o(n) {
      M(o, n), s = !1;
    },
    d(n) {
      n && P(e), o && o.d(n), t[9](null);
    }
  };
}
function Ke(t) {
  let e, s, l, o, n = (
    /*$$slots*/
    t[4].default && K(t)
  );
  return {
    c() {
      e = oe("react-portal-target"), s = Ge(), n && n.c(), l = X(), this.h();
    },
    l(r) {
      e = re(r, "REACT-PORTAL-TARGET", {
        class: !0
      }), ne(e).forEach(P), s = Ae(r), n && n.l(r), l = X(), this.h();
    },
    h() {
      le(e, "class", "svelte-1rt0kpf");
    },
    m(r, i) {
      O(r, e, i), t[8](e), O(r, s, i), n && n.m(r, i), O(r, l, i), o = !0;
    },
    p(r, [i]) {
      /*$$slots*/
      r[4].default ? n ? (n.p(r, i), i & /*$$slots*/
      16 && T(n, 1)) : (n = K(r), n.c(), T(n, 1), n.m(l.parentNode, l)) : n && (He(), M(n, 1, 1, () => {
        n = null;
      }), Ne());
    },
    i(r) {
      o || (T(n), o = !0);
    },
    o(r) {
      M(n), o = !1;
    },
    d(r) {
      r && (P(e), P(s), P(l)), t[8](null), n && n.d(r);
    }
  };
}
function Q(t) {
  const {
    svelteInit: e,
    ...s
  } = t;
  return s;
}
function Qe(t, e, s) {
  let l, o, {
    $$slots: n = {},
    $$scope: r
  } = e;
  const i = We(n);
  let {
    svelteInit: a
  } = e;
  const w = k(Q(e)), m = k();
  J(t, m, (u) => s(0, l = u));
  const c = k();
  J(t, c, (u) => s(1, o = u));
  const p = [], d = Je("$$ms-gr-react-wrapper"), {
    slotKey: b,
    slotIndex: f,
    subSlotIndex: h
  } = me() || {}, g = a({
    parent: d,
    props: w,
    target: m,
    slot: c,
    slotKey: b,
    slotIndex: f,
    subSlotIndex: h,
    onDestroy(u) {
      p.push(u);
    }
  });
  Ye("$$ms-gr-react-wrapper", g), Ve(() => {
    w.set(Q(e));
  }), Xe(() => {
    p.forEach((u) => u());
  });
  function C(u) {
    V[u ? "unshift" : "push"](() => {
      l = u, m.set(l);
    });
  }
  function E(u) {
    V[u ? "unshift" : "push"](() => {
      o = u, c.set(o);
    });
  }
  return t.$$set = (u) => {
    s(17, e = q(q({}, e), Y(u))), "svelteInit" in u && s(5, a = u.svelteInit), "$$scope" in u && s(6, r = u.$$scope);
  }, e = Y(e), [l, o, m, c, i, a, r, n, C, E];
}
class Ze extends Le {
  constructor(e) {
    super(), Ue(this, e, Qe, Ke, ze, {
      svelteInit: 5
    });
  }
}
const Z = window.ms_globals.rerender, N = window.ms_globals.tree;
function $e(t, e = {}) {
  function s(l) {
    const o = k(), n = new Ze({
      ...l,
      props: {
        svelteInit(r) {
          window.ms_globals.autokey += 1;
          const i = {
            key: window.ms_globals.autokey,
            svelteInstance: o,
            reactComponent: t,
            props: r.props,
            slot: r.slot,
            target: r.target,
            slotIndex: r.slotIndex,
            subSlotIndex: r.subSlotIndex,
            ignore: e.ignore,
            slotKey: r.slotKey,
            nodes: []
          }, a = r.parent ?? N;
          return a.nodes = [...a.nodes, i], Z({
            createPortal: A,
            node: N
          }), r.onDestroy(() => {
            a.nodes = a.nodes.filter((w) => w.svelteInstance !== o), Z({
              createPortal: A,
              node: N
            });
          }), i;
        },
        ...l.props
      }
    });
    return o.set(n), n;
  }
  return new Promise((l) => {
    window.ms_globals.initializePromise.then(() => {
      l(s);
    });
  });
}
const et = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function tt(t) {
  return t ? Object.keys(t).reduce((e, s) => {
    const l = t[s];
    return e[s] = nt(s, l), e;
  }, {}) : {};
}
function nt(t, e) {
  return typeof e == "number" && !et.includes(t) ? e + "px" : e;
}
function B(t) {
  const e = [], s = t.cloneNode(!1);
  if (t._reactElement) {
    const o = I.Children.toArray(t._reactElement.props.children).map((n) => {
      if (I.isValidElement(n) && n.props.__slot__) {
        const {
          portals: r,
          clonedElement: i
        } = B(n.props.el);
        return I.cloneElement(n, {
          ...n.props,
          el: i,
          children: [...I.Children.toArray(n.props.children), ...r]
        });
      }
      return null;
    });
    return o.originalChildren = t._reactElement.props.children, e.push(A(I.cloneElement(t._reactElement, {
      ...t._reactElement.props,
      children: o
    }), s)), {
      clonedElement: s,
      portals: e
    };
  }
  Object.keys(t.getEventListeners()).forEach((o) => {
    t.getEventListeners(o).forEach(({
      listener: r,
      type: i,
      useCapture: a
    }) => {
      s.addEventListener(i, r, a);
    });
  });
  const l = Array.from(t.childNodes);
  for (let o = 0; o < l.length; o++) {
    const n = l[o];
    if (n.nodeType === 1) {
      const {
        clonedElement: r,
        portals: i
      } = B(n);
      e.push(...i), s.appendChild(r);
    } else n.nodeType === 3 && s.appendChild(n.cloneNode());
  }
  return {
    clonedElement: s,
    portals: e
  };
}
function rt(t, e) {
  t && (typeof t == "function" ? t(e) : t.current = e);
}
const F = ie(({
  slot: t,
  clone: e,
  className: s,
  style: l,
  observeAttributes: o
}, n) => {
  const r = ce(), [i, a] = ae([]), {
    forceClone: w
  } = he(), m = w ? !0 : e;
  return de(() => {
    var b;
    if (!r.current || !t)
      return;
    let c = t;
    function p() {
      let f = c;
      if (c.tagName.toLowerCase() === "svelte-slot" && c.children.length === 1 && c.children[0] && (f = c.children[0], f.tagName.toLowerCase() === "react-portal-target" && f.children[0] && (f = f.children[0])), rt(n, f), s && f.classList.add(...s.split(" ")), l) {
        const h = tt(l);
        Object.keys(h).forEach((g) => {
          f.style[g] = h[g];
        });
      }
    }
    let d = null;
    if (m && window.MutationObserver) {
      let f = function() {
        var E, u, y;
        (E = r.current) != null && E.contains(c) && ((u = r.current) == null || u.removeChild(c));
        const {
          portals: g,
          clonedElement: C
        } = B(t);
        c = C, a(g), c.style.display = "contents", p(), (y = r.current) == null || y.appendChild(c);
      };
      f();
      const h = Re(() => {
        f(), d == null || d.disconnect(), d == null || d.observe(t, {
          childList: !0,
          subtree: !0,
          attributes: o
        });
      }, 50);
      d = new window.MutationObserver(h), d.observe(t, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      c.style.display = "contents", p(), (b = r.current) == null || b.appendChild(c);
    return () => {
      var f, h;
      c.style.display = "", (f = r.current) != null && f.contains(c) && ((h = r.current) == null || h.removeChild(c)), d == null || d.disconnect();
    };
  }, [t, m, s, l, n, o]), I.createElement("react-child", {
    ref: r,
    style: {
      display: "contents"
    }
  }, ...i);
});
function se(t, e, s) {
  const l = t.filter(Boolean);
  if (l.length !== 0)
    return l.map((o, n) => {
      var w;
      if (typeof o != "object")
        return e != null && e.fallback ? e.fallback(o) : o;
      const r = {
        ...o.props,
        key: ((w = o.props) == null ? void 0 : w.key) ?? (s ? `${s}-${n}` : `${n}`)
      };
      let i = r;
      Object.keys(o.slots).forEach((m) => {
        if (!o.slots[m] || !(o.slots[m] instanceof Element) && !o.slots[m].el)
          return;
        const c = m.split(".");
        c.forEach((g, C) => {
          i[g] || (i[g] = {}), C !== c.length - 1 && (i = r[g]);
        });
        const p = o.slots[m];
        let d, b, f = (e == null ? void 0 : e.clone) ?? !1, h = e == null ? void 0 : e.forceClone;
        p instanceof Element ? d = p : (d = p.el, b = p.callback, f = p.clone ?? f, h = p.forceClone ?? h), h = h ?? !!b, i[c[c.length - 1]] = d ? b ? (...g) => (b(c[c.length - 1], g), /* @__PURE__ */ v.jsx(D, {
          params: g,
          forceClone: h,
          children: /* @__PURE__ */ v.jsx(F, {
            slot: d,
            clone: f
          })
        })) : /* @__PURE__ */ v.jsx(D, {
          forceClone: h,
          children: /* @__PURE__ */ v.jsx(F, {
            slot: d,
            clone: f
          })
        }) : i[c[c.length - 1]], i = r;
      });
      const a = (e == null ? void 0 : e.children) || "children";
      return o[a] ? r[a] = se(o[a], e, `${n}`) : e != null && e.children && (r[a] = void 0, Reflect.deleteProperty(r, a)), r;
    });
}
function H(t, e) {
  return t ? /* @__PURE__ */ v.jsx(F, {
    slot: t,
    clone: e == null ? void 0 : e.clone
  }) : null;
}
function $({
  key: t,
  slots: e,
  targets: s
}, l) {
  return e[t] ? (...o) => s ? s.map((n, r) => /* @__PURE__ */ v.jsx(D, {
    params: o,
    forceClone: (l == null ? void 0 : l.forceClone) ?? !0,
    children: H(n, {
      clone: !0,
      ...l
    })
  }, r)) : /* @__PURE__ */ v.jsx(D, {
    params: o,
    forceClone: (l == null ? void 0 : l.forceClone) ?? !0,
    children: H(e[t], {
      clone: !0,
      ...l
    })
  }) : void 0;
}
const {
  useItems: ot,
  withItemsContextProvider: lt,
  ItemHandler: ct
} = S("antd-menu-items"), {
  useItems: at,
  withItemsContextProvider: dt,
  ItemHandler: st
} = S("antd-table-columns");
S("antd-table-row-selection-selections");
S("antd-table-row-selection");
S("antd-table-expandable");
const ut = $e(lt(["filterDropdownProps.menu.items"], ({
  setSlotParams: t,
  itemSlots: e,
  ...s
}) => {
  const {
    items: {
      "filterDropdownProps.menu.items": l
    }
  } = ot();
  return /* @__PURE__ */ v.jsx(st, {
    ...s,
    itemProps: (o) => {
      var i, a, w, m, c, p, d, b;
      const n = {
        ...((i = o.filterDropdownProps) == null ? void 0 : i.menu) || {},
        items: (w = (a = o.filterDropdownProps) == null ? void 0 : a.menu) != null && w.items || l.length > 0 ? se(l, {
          clone: !0
        }) : void 0,
        expandIcon: $({
          setSlotParams: t,
          slots: e,
          key: "filterDropdownProps.menu.expandIcon"
        }, {
          clone: !0
        }) || ((c = (m = o.filterDropdownProps) == null ? void 0 : m.menu) == null ? void 0 : c.expandIcon),
        overflowedIndicator: H(e["filterDropdownProps.menu.overflowedIndicator"]) || ((d = (p = o.filterDropdownProps) == null ? void 0 : p.menu) == null ? void 0 : d.overflowedIndicator)
      }, r = {
        ...o.filterDropdownProps || {},
        dropdownRender: e["filterDropdownProps.dropdownRender"] ? $({
          setSlotParams: t,
          slots: e,
          key: "filterDropdownProps.dropdownRender"
        }, {
          clone: !0
        }) : pe((b = o.filterDropdownProps) == null ? void 0 : b.dropdownRender),
        menu: Object.values(n).filter(Boolean).length > 0 ? n : void 0
      };
      return {
        ...o,
        filterDropdownProps: Object.values(r).filter(Boolean).length > 0 ? r : void 0
      };
    }
  });
}));
export {
  ut as TableColumn,
  ut as default
};
